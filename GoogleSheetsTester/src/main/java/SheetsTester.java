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

import org.eclipse.jetty.util.IO;
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
import  java.text.SimpleDateFormat;

import javax.security.auth.login.LoginContext;
import java.util.HashMap;


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

    // need to fix this method to take any number of rows to read
    public static void readData(String range, int row1, int row2) throws IOException, GeneralSecurityException {
        /*This methos takes in a range from the spreadsheet and row indexes to read and print into the console*/
        ValueRange response = sheetsService.spreadsheets().values() // ValueRange object returns a list of values from the range
                .get(spreadsheetId, range).execute();

        List<List<Object>> values = response.getValues(); // Values will be a 2D list, each list being a row

        // To read data, first check if the spreadsheet is empty or not
        if(values == null || values.isEmpty()){
            System.out.println("No data found.");
        }else{
            for(List row : values){ // loop over each row in 2D values list
                System.out.printf("%s : %s\n",row.get(row1),row.get(row2)); // rows are 0 indexed fstring format (?)
            }
        }

    }

    public static void appendData(String range,String data,String insertDataOption) throws IOException, GeneralSecurityException{
        /* This method appends new data in a given range */
        sheetsService = getSheetsService();
        Object[] dataArray = data.split(","); // splits data by the commas to be inserted into separate cells

        // To write new data (here appending to bottom of spreadsheet), must create new ValueRange as a 2D list
        ValueRange newValues = new ValueRange().setValues( // each list being a row
                Arrays.asList(Arrays.asList(dataArray)) // each element(here strings) being a column in the row

        );

        AppendValuesResponse append = sheetsService.spreadsheets().values() // Sends an append request which returns an append result
                .append(spreadsheetId, range, newValues).setValueInputOption("USER_ENTERED") // Can specify range as entire sheet or specific cell to start data
                .setInsertDataOption(insertDataOption).setIncludeValuesInResponse(true).execute();

    }

    public static void updateData(String range, String data)throws IOException, GeneralSecurityException{
        /* This method updates existing data in a cell */

        sheetsService = getSheetsService();
        ValueRange updateValues = new ValueRange().setValues( // each list being a row
                Arrays.asList(Arrays.asList(data)) // each element(here strings) being a column in the row

        );

        UpdateValuesResponse update = sheetsService.spreadsheets().values() // Sends an update request which returns an append result
                .update(spreadsheetId, range, updateValues).setValueInputOption("RAW") // Specify range as one cell
                .execute();

    }

    public static void deleteData(int sheetId,int startIndex,String dimension)throws IOException, GeneralSecurityException{
        /* This method deletes data given a start index and dimension (rows or columns) to delete */
        sheetsService = getSheetsService();
        DeleteDimensionRequest delete = new DeleteDimensionRequest()
                .setRange(
                        new DimensionRange()
                                .setSheetId(sheetId) // sheet ID at end of this spreadsheets URL is 0
                                .setDimension(dimension) // want to delete an entire "ROWS" or "COLUMNS"
                                .setStartIndex(startIndex) // rows are 0 indexed, this will delete row 15
                );

        // We are sending a list of requests to do BatchUpdate
        List<Request> request = new ArrayList<>();
        request.add(new Request().setDeleteDimension(delete)); // in the list, add the DeleteDimensionRequest 'delete'


        // In the batchupdate request, set request to the list of requests created
        BatchUpdateSpreadsheetRequest body = new BatchUpdateSpreadsheetRequest().setRequests(request);

        sheetsService.spreadsheets().batchUpdate(spreadsheetId,body).execute(); // use sheetsService to actually call batchupdate

    }

    public static void report(int content) throws IOException,GeneralSecurityException{
        /* Report specific data to the console (e.g. Total income, total spendings, etc) */
        String range = "";
        HashMap <Integer,String> map = new HashMap<Integer,String> ();

        if (content == 1){ // total income
            range = "Sheet1!B2";
        }
        readData(range,0,0);
    }

    public static void main(String[] args) throws IOException,GeneralSecurityException{
        sheetsService = getSheetsService();
        String range = "Sheet1!C3:D";

//        readData(range,0,1);

//        report(1);
        //appendData("Sheet1", "How about,this", "INSERT_ROWS");

//        updateData("J1", "HEllo");
//
//       deleteData(0, 10, "COLUMNS");

    }



}
