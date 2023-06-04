package io.pop.lld.creational.singleton;

public class SingleThreadedSingleton {
    private static SingleThreadedSingleton INSTANCE;

    public static SingleThreadedSingleton getInstance() {
        if (INSTANCE != null) {
            return INSTANCE;
        }
        INSTANCE = new SingleThreadedSingleton();
        return INSTANCE;
    }

    private SingleThreadedSingleton() {
        System.out.println("constructed SingleThreadedSingleton");
    }

    public void execute() {
        System.out.println("executing SingleThreadedSingleton");
    }
}
