package io.pop.lld.creational.singleton;

public class DoubleCheckedLockingSingleton {
    private static DoubleCheckedLockingSingleton INSTANCE;

    public static DoubleCheckedLockingSingleton getInstance() {
        if (INSTANCE != null) {
            return INSTANCE;
        }

        synchronized(DoubleCheckedLockingSingleton.class) {
            if (INSTANCE != null) {
                return INSTANCE;
            }

            INSTANCE = new DoubleCheckedLockingSingleton();
            return INSTANCE;
        }
    }

    private DoubleCheckedLockingSingleton() {
        System.out.println("constructed DoubleCheckedLockingSingleton");
    }

    public void execute() {
        System.out.println("executing DoubleCheckedLockingSingleton");
    }
}
