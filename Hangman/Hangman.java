import java.util.Scanner;

class Hangman{
    public static void main(String[] args) {
        Scanner key = new Scanner(System.in); 

        String word = Generator.randomWord(); // Pulls a random word from the WordBank.txt

        System.out.println("Guess the word: ");
        String blanks[] = Generator.createBlanks(word);

        boolean playing = false;
        
       while (playing==false){
            String user = key.nextLine(); // user guesses a letter

            if(word.contains(user)){ // if the user guessed a correct letter
                System.out.println("The word contains the letter: " + user);

                blanks = Generator.replaceBlanks(word,blanks,user.charAt(0)); // replace blanks to letter

            } else{
                System.out.println("The word does not contain the letter: " + user);
            }   
            playing = Generator.checkAnswer(word, blanks); // compare the status of the blanks to determine if they completed the word
        }
        key.close();

        System.out.println("You guessed the word: " + word);
    }
}