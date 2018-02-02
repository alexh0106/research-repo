import java.util.*;
import java.io.*;
public class CoReader {
   public static void main(String[] args) throws FileNotFoundException {
      Scanner fileRead = new Scanner(new File("companies.txt"));
      PrintStream fileWriter = new PrintStream(new File("formattedCo.txt"));
      while(fileRead.hasNextLine()) {
         String line = fileRead.nextLine();
         for(int i = 0; i < line.length(); i++) {
            if (line.charAt(i) == '\t') {
               String name = line.substring(0,i);
               if ( name.charAt(name.length() - 1) == ' ') {
                  name = name.substring(0, name.length() -2);
               }
               fileWriter.println(name);
               line = line.substring(i + 1);
               i = 0;
            } 
         }
      }
   }
}