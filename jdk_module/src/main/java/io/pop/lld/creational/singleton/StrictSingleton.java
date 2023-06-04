package io.pop.lld.creational.singleton;

import java.io.*;

public class StrictSingleton implements Serializable, Cloneable {
  private static final StrictSingleton INSTANCE = new StrictSingleton();

  public static StrictSingleton getInstance() {
    return INSTANCE;
  }

  private StrictSingleton() {
    System.out.println("constructed StrictSingleton");
  }

  public void exeucte() {
    System.out.println("executing StrictSingleton");
  }

  protected Object readResolve() {
    return INSTANCE;
  }

  @Override
  protected Object clone() throws CloneNotSupportedException {
    throw new CloneNotSupportedException();
  }
}
