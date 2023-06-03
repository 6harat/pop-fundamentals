package io.pop.lld.creational.factory.impl;

import io.pop.lld.creational.factory.Formatter;
import io.pop.lld.creational.factory.FormatterFactory;

public class DefaultFormatterFactory implements FormatterFactory {
    @Override
    public Formatter createFormatter(final String separator) {
        switch (separator) {
            case "tab": return new TabBreakFormatter();
            default: return new SpaceBreakFormatter();
        }
    }
}
