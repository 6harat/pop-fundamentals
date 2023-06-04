package io.pop.lld.creational.singleton;

public final class BillPughSingleton {
    public static BillPughSingleton getInstance() {
        return Holder.INSTANCE;
    }

    private BillPughSingleton() {
        System.out.println("constructed BillPughSingleton");
    }

    public void execute() {
        System.out.println("executing BillPughSingleton");
    }

    private static final class Holder {
        private static BillPughSingleton INSTANCE = new BillPughSingleton();

        private Holder() {
            System.out.println("constructed BillPughSingleton.Holder");
        }
    }
}
