package io.pop.lld.behavioral.chain_of_responsibility.impl;

import io.pop.lld.behavioral.chain_of_responsibility.Handler;
import io.pop.lld.behavioral.chain_of_responsibility.domain.Request;
import io.pop.lld.behavioral.chain_of_responsibility.domain.Response;

public abstract class AbstractHandler implements Handler<Request, Response> {
  protected Handler<Request, Response> nextHandler;

  @Override
  public void setNext(final Handler<Request, Response> handler) {
    nextHandler = handler;
  }
}
