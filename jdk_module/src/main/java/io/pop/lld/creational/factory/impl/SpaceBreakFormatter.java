package io.pop.lld.creational.factory.impl;

import io.pop.lld.creational.factory.Formatter;

public class SpaceBreakFormatter implements Formatter {
    @Override
    public String format(final String input) {
        return input.replaceAll("\\s+", "\\n");
    }
}
