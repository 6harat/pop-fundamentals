package io.pop.lld.behavioral.strategy;

public interface Search<Req, Res> {
  String name();

  Res execute(final Req request);
}
