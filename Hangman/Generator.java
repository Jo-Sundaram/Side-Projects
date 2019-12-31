import java.util.Random;

class Generator {
	
	public static int fileLenght(){
        
        /* This method returns the number of lines in a file*/

        IO.openInputFile("Wordbank.txt");
		int numlines = 0;
		
        String line = IO.readLine();

        while(line != null){
            numlines++;
            line=IO.readLine();
        }

        IO.closeInputFile();


		return numlines;
		
	}

    public static String randomWord(){
        /* This method reads the contents of a file and stores in an array
        Return random element from array    */

        Random random = new Random();

        int fileLength = fileLenght(); // get number of lines in word bank

        String[] words = new String[fileLength]; // create array of words to store word bank

        IO.openInputFile("WordBank.txt");

        for(int i = 0; i < fileLength-1; i++){ // store each word as element in array
            words[i] = IO.readLine();
        }

        IO.closeInputFile();

        int randomWord = random.nextInt(fileLength);

        
        return words[randomWord];

    }

    public static String[] createBlanks(String mysteryWord){
        /* This method prints a string of blanks '_' for the given mystery word */

        String[] blanks = new String [mysteryWord.length()];

        for(int i = 0; i < mysteryWord.length(); i++){
            
            blanks[i] = "_";


            System.out.print(blanks[i]+" ");

        }

        System.out.println();
        
        return blanks;

    }

    public static String[] replaceBlanks(String mysteryWord,String[] blanks, char token){
        /* This method replaced the blanks with the user's inputted letter (token) */

        String[] newBlanks = blanks;

        for(int i = 0; i < mysteryWord.length(); i++){
            char letter = mysteryWord.charAt(i); // Track each letter of the word as a char

            if (token == letter){ // the the current letter == the user's guessed letter

                newBlanks[i] = Character.toString(token); // replace the blanks with the letter

            }

            System.out.print(newBlanks[i]+" ");

        }

        System.out.println();

        return newBlanks;


        
    }

    public static boolean checkAnswer(String mysteryword, String[] blanks){
        /* This method compares the user's answers to the mystery word and determines when they completed the word */

        String[] letters = new String[mysteryword.length()];

        
        for(int i = 0; i < mysteryword.length(); i++){

            letters[i] = Character.toString(mysteryword.charAt(i));

            if(letters[i].equalsIgnoreCase(blanks[i])){
                continue;
            }else{
                return false;
            }

        }

        return true;

    }

}