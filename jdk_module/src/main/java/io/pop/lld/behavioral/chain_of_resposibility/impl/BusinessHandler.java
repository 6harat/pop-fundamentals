package io.pop.lld.behavioral.chain_of_responsibility.impl;

import io.pop.lld.behavioral.chain_of_responsibility.domain.Request;
import io.pop.lld.behavioral.chain_of_responsibility.domain.Response;

public class BusinessHandler extends AbstractHandler {
    @Override
    public void handle(final Request request, final Response response) {
        response.setResult("completed");
        if (nextHandler == null) {
            return;
        }
        nextHandler.handle(request, response);
    }
}
