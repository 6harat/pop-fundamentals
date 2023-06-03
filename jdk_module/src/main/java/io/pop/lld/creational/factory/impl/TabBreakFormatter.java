package io.pop.lld.creational.factory.impl;

import io.pop.lld.creational.factory.Formatter;

public class TabBreakFormatter implements Formatter {
  @Override
  public String format(final String input) {
    return input.replaceAll("\\t+", "\\n");
  }
}
