// import java.util.Scanner;
public class firstpra{
    public static void main(String[] args){
        // System.out.println("Enter your name");
        //  Scanner scan =new Scanner(System.in);
        //  String name =scan.next();
        //  System.out.println( "your name is " + name);

        //  System.out.println("Enter your age");
        //  int age=scan.nextInt();
        //  System.out.println("your age is "+ age);
        //   System.out.println(name + " is " + age  +  "years old");
           int n = 17;
          for(int i=0;i<n; i++){
          for(int j = 0; j<n; j++)
          {
              if(i==0 || j==0 || j==n-1 || i == n-1 || i+j==n/2 || j-i==n/2 || i==n/2 || (i+j>=n/2 & j-i<n/2 & i<n/2))
              {
                  System.out.print("*");
              }
              else{
                  System.out.print(" ");
              }         
        }
        System.out.println();
    }
}
}