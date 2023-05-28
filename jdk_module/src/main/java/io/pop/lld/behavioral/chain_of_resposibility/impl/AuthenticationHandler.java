package io.pop.lld.behavioral.chain_of_responsibility.impl;

import io.pop.lld.behavioral.chain_of_responsibility.domain.Request;
import io.pop.lld.behavioral.chain_of_responsibility.domain.Response;

public class AuthenticationHandler extends AbstractHandler {
    @Override
    public void handle(final Request request, final Response response) {
        if (request.getUser() == null) {
            response.setError("not authenticated");
            return;
        }

        if (nextHandler == null) {
            return;
        }

        nextHandler.handle(request, response);
    }
}
