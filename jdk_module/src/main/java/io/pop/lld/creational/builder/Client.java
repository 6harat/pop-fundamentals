package io.pop.lld.creational.builder;

import java.util.*;

public class Client {
    private List<String> targets;
    private int poolSize;

    public List<String> getTargets() {
        return targets;
    }

    public void setTargets(final List<String> targets) {
        this.targets = targets;
    }

    public int getPoolSize() {
        return poolSize;
    }

    public void setPoolSize(final int poolSize) {
        this.poolSize = poolSize;
    }
}
