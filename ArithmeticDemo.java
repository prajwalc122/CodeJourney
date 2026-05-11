class ArithmeticDemo{
    public static void main(String args[]) {

        try {
            int a = 10;
            int b = 0;

            int c = a / b;

            System.out.println(c);
        }

        catch(ArithmeticException e) {
            System.out.println("Cannot divide by zero");
        }

        System.out.println("Program ended");
    }
}