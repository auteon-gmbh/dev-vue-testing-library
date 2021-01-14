import { render } from '@testing-library/vue'
import userEvent from '@testing-library/user-event'
import HelloWorld from './HelloWorld.vue'

describe('Hello World', () => {
  it('should disable the input by default.', () => {
    const { getByRole } = render(HelloWorld)

    const input = getByRole('textbox', { name: 'Username' })

    expect(input).toBeDisabled()
  })

  it('should be possible to click the button', async () => {
    const { getByRole } = render(HelloWorld)

    const button = getByRole('button', { name: 'Click me' })
    const input = getByRole('textbox', { name: 'Username' })

    await userEvent.click(button)

    expect(input).not.toBeDisabled()
  })
})
