import java.util.Scanner;

class Hangman{


    public static void main(String[] args) {
        Scanner key = new Scanner(System.in); 
        String word = Generator.randomWord();

        System.out.println(word);
        String blanks[] = Generator.createBlanks(word);

        boolean playing = false;
        
        String check;

       while (playing==false){
            String user = key.nextLine(); // user guesses a letter

            if(word.contains(user)){
                System.out.println(word + " contains the letter: " + user);

                blanks = Generator.replaceBlanks(word,blanks,user.charAt(0)); // replace blanks to letter
                check = Generator.checkAnswer(word, blanks); // need to fix


            } else{
                System.out.println(word + " does not contain the letter: " + user);

            }   


                  

        }
        key.close();
    
    }


}