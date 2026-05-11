class Animal {

    // Parent class method
    void sound() {
        System.out.println("Animal makes sound");
    }
}

class Dog extends Animal {

    // Overriding parent method
    void sound() {
        System.out.println("Dog barks");
    }
}

class Mains{
    public static void main(String args[]) {

        Dog d = new Dog();

        // Calling overridden method
        d.sound();
    }
}