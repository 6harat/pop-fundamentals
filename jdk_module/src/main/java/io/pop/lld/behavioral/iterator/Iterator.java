package io.pop.lld.behavioral.iterator;

public interface Iterator<T> {
  T next();

  boolean hasNext();
}
