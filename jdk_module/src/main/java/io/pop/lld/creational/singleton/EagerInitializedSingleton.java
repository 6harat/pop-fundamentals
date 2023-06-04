package io.pop.lld.creational.singleton;

public class EagerInitializedSingleton {
    private static final EagerInitializedSingleton INSTANCE = new EagerInitializedSingleton();

    public static EagerInitializedSingleton getInstance() {
        return INSTANCE;
    }

    private EagerInitializedSingleton() {
        System.out.println("constructed EagerInitializedSingleton");
    }

    public void execute() {
        System.out.println("executing EagerInitializedSingleton");
    }
}
