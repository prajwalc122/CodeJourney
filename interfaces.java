// Interface declaration
interface Animal {

    // abstract method
    void sound();
}

// Class implementing interface
class Dog implements Animal {

    // method implementation
    public void sound() {
        System.out.println("Dog barks");
    }
}

// Main class
public class interfaces
{

    public static void main(String[] args) {

        // creating object
        Dog d = new Dog();

        // calling method
        d.sound();
    }
}