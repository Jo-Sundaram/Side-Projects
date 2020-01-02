import com.google.api.client.auth.oauth2.Credential;
import com.google.api.client.extensions.java6.auth.oauth2.AuthorizationCodeInstalledApp;
import com.google.api.client.extensions.jetty.auth.oauth2.LocalServerReceiver;
import com.google.api.client.googleapis.auth.oauth2.GoogleAuthorizationCodeFlow;
import com.google.api.client.googleapis.auth.oauth2.GoogleClientSecrets;
import com.google.api.client.googleapis.javanet.GoogleNetHttpTransport;
import com.google.api.client.http.javanet.NetHttpTransport;
import com.google.api.client.json.JsonFactory;
import com.google.api.client.json.jackson2.JacksonFactory;
import com.google.api.client.util.Value;
import com.google.api.client.util.store.FileDataStoreFactory;
import com.google.api.services.sheets.v4.Sheets;
import com.google.api.services.sheets.v4.SheetsScopes;
import com.google.api.services.sheets.v4.model.*;

import org.omg.CORBA.portable.ApplicationException;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.security.GeneralSecurityException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import javax.security.auth.login.LoginContext;


public class SheetsTester{
    private static Sheets sheetsService; // service to access google sheets SDK
    private static String APPLICATION_NAME = "Sheets tester";
    private static String spreadsheetId = "1uBHFsTpwllzqe8BUi4IZaVCJvpBZvshISpHUPaJvIfw"; // ID unique to spreadsheet

    private static Credential authorize() throws IOException, GeneralSecurityException{
        /*This method gets the credentials for spreadsheets and returns the credential
        * to grant access to the spreadsheet*/

        InputStream in = SheetsTester.class.getResourceAsStream("/credentials.json");
        GoogleClientSecrets clientSecrets = GoogleClientSecrets.load(
            JacksonFactory.getDefaultInstance(), new InputStreamReader(in));

        List<String> scopes = Arrays.asList(SheetsScopes.SPREADSHEETS);// scopes to grant access to (just spreadsheets in this case)

        GoogleAuthorizationCodeFlow flow = new GoogleAuthorizationCodeFlow.Builder(
            GoogleNetHttpTransport.newTrustedTransport(), JacksonFactory.getDefaultInstance(), clientSecrets, scopes)
            .setDataStoreFactory(new FileDataStoreFactory(new java.io.File("tokens")))
            .setAccessType("offline")
            .build();

        Credential credential = new AuthorizationCodeInstalledApp(
            flow, new LocalServerReceiver()).authorize("user");

        return credential;


    }


    public static Sheets getSheetsService()  throws IOException, GeneralSecurityException{
        /*This method gets the sheets service to be used*/

        Credential credential = authorize(); // get credientials using the authorize() method above

        return new Sheets.Builder(GoogleNetHttpTransport.newTrustedTransport(), JacksonFactory.getDefaultInstance(), credential)
        .setApplicationName(APPLICATION_NAME).build();


    }

    public static void main(String[] args) throws IOException,GeneralSecurityException{
        sheetsService = getSheetsService();
        String range = "Sheet1!A1:B";

        ValueRange response = sheetsService.spreadsheets().values() // ValueRange object returns a list of values from the range
        .get(spreadsheetId, range).execute();

        List<List<Object>> values = response.getValues(); // Values will be a 2D list, each list being a row

        if(values == null || values.isEmpty()){ // To read data, first check if the spreadsheet is empty or not
            System.out.println("No data found.");
        }else{
            for(List row : values){ // loop over each row in 2D values list
                System.out.printf("%s : %s\n",row.get(0),row.get(1)); // rows are 0 indexed fstring format (?)
            }
        }


        // To write new data (here appending to bottom of spreadsheet), must create new ValueRange as a 2D list
        ValueRange newValues = new ValueRange().setValues( // each list being a row
            Arrays.asList(Arrays.asList("This","is","new","data")) // each element(here strings) being a column in the row

        );

        AppendValuesResponse append = sheetsService.spreadsheets().values() // Sends an append request which returns an append result
        .append(spreadsheetId, "Sheet1", newValues).setValueInputOption("USER_ENTERED") // Can specify range as entire sheet
        .setInsertDataOption("INSERT_ROWS").setIncludeValuesInResponse(true).execute();


        // To update existing data, same ValuesResponse 2D list
        ValueRange updateValues = new ValueRange().setValues( // each list being a row
                Arrays.asList(Arrays.asList("updated")) // each element(here strings) being a column in the row

        );


        UpdateValuesResponse update = sheetsService.spreadsheets().values() // Sends an update request which returns an append result
                .update(spreadsheetId, "C14", updateValues).setValueInputOption("RAW") // Specify range as one cell
                .execute();



        // To delete existing data, setup DeleteDimensionRequest
        DeleteDimensionRequest delete = new DeleteDimensionRequest()
                .setRange(
                        new DimensionRange()
                        .setSheetId(0) // sheet ID at end of this spreadsheets URL is 0
                        .setDimension("ROWS") // want to delete an entire row
                        .setStartIndex(14) // rows are 0 indexed, this will delete row 15
                );

        // We are sending a list of requests to do BatchUpdate
        List<Request> request = new ArrayList<>();
        request.add(new Request().setDeleteDimension(delete)); // in the list, add the DeleteDimensionRequest 'delete'


        // In the batchupdate request, set request to the list of requests created
        BatchUpdateSpreadsheetRequest body = new BatchUpdateSpreadsheetRequest().setRequests(request);

        sheetsService.spreadsheets().batchUpdate(spreadsheetId,body).execute(); // use sheetsService to actually call batchupdate



    }



}
