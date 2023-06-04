package io.pop.lld.creational.singleton;

public class SynchronizedSingleton {
    private static SynchronizedSingleton INSTANCE;

    public synchronized static SynchronizedSingleton getInstance() {
        if (INSTANCE != null) {
            return INSTANCE;
        }
        INSTANCE = new SynchronizedSingleton();
        return INSTANCE;
    }

    private SynchronizedSingleton() {
        System.out.println("constructed SynchronizedSingleton");
    }

    public void execute() {
        System.out.println("executing SynchronizedSingleton");
    }
}
