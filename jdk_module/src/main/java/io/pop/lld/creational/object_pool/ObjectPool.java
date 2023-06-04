package io.pop.lld.creational.object_pool;

import java.util.*;

public interface ObjectPool<T> {
    Optional<T> acquire();
    void release(final T object);
    int getMaxPoolSize();
    ObjectFactory<T> getObjectFactory();
}
