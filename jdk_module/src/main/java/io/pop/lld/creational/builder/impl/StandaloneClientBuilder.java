package io.pop.lld.creational.builder.impl;

import java.util.*;
import io.pop.lld.creational.builder.Client;
import io.pop.lld.creational.builder.ClientBuilder;

public class StandaloneClientBuilder implements ClientBuilder {
    private Client client = new Client();

    @Override
    public Client build() {
        return client;
    }

    @Override
    public void reset() {
        client = new Client();
    }

    @Override
    public void setTarget() {
        client.setTargets(List.of("hello"));
    }

    @Override
    public void setPoolSize() {
        client.setPoolSize(1);
    }
}
