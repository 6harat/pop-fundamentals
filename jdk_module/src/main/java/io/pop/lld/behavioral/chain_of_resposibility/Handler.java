package io.pop.lld.behavioral.chain_of_responsibility;

public interface Handler<Req, Res> {
  void setNext(final Handler<Req, Res> h);
  void handle(final Req request, final Res response);
}
