package io.pop.lld.behavioral.observer.domain;

import io.pop.lld.behavioral.observer.Event;

public class SuccessEvent implements Event {
  private static final String NAME = "success";

  public String name() {
    return NAME;
  }
}
