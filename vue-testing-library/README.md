# dev-vue-testing-library

This is a companion repository to a small talk I held to introduce [`@testing-library`](https://testing-library.com/) to the team on Jan. 14 2020.

## Storyline

The test code in `HelloWorld-vue-testing-library.spec.ts` is working.
However, since it is strongly coupled to the structure of the component by directly referencing `input` and `button` elements the tests can break even though the functionality still works.
For instance, by adding another input at the beginning of the template in `HelloWorld.vue` you can break the tests even though the code still works.
This isn't optimal.

By introducing [`@testing-library/vue`](https://testing-library.com/docs/vue-testing-library/intro) we need to write tests with a different perspective.
`@testing-library` forces us to interact with our components similar to how our users would.
For instance, we determine which button to click based on the text on the button.
By doing so we decouple our tests from our implementation.
All code that produces a semantically correct DOM structure will work.
Only when we change core functionality (e.g. the button label) our tests will fail.
This makes sense because by changing the name of a button we might also change its meaning.

## Visual testing

In the discussion following the talk a question came up whether I would test UI (pixel) in a similar way.
For me this is solely about functionality.
To ensure UIs are correct we can use tools like [`percy`](https://percy.io/) that work nicely together with other tools like [Vercel](https://vercel.com/).

## Further reading

I am a big fan of TDD and testing code.
I, therefore, have blogged about it a couple of times.
Here are some articles:

- [Tests that help you find defects faster](https://philgiese.com/post/tests-that-help-you-find-defects-faster)
- [Using GitHub Actions and Vercel for end-to-end tests](https://philgiese.com/post/e2e-with-vercel)
- [The religion of test-driven development](https://philgiese.com/post/the-religion-of-test-driven-development)
