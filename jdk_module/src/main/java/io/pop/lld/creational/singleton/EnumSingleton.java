package io.pop.lld.creational.singleton;

public enum EnumSingleton {
  INSTANCE;

  private EnumSingleton() {
    System.out.println("constructed EnumSingleton");
  }

  public void exeucte() {
    System.out.println("executing EnumSingleton");
  }
}
