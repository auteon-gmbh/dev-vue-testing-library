import { render } from '@testing-library/vue'
import userEvent from '@testing-library/user-event'
import HelloWorld from './HelloWorld.vue'

describe('Hello World', () => {
  it('should disable the input by default.', () => {
    const { getByRole } = render(HelloWorld)

    const input = getByRole('textbox', { name: 'Enter your username' })

    expect(input).toBeDisabled()
  })

  it('should be possible to click the button', async () => {
    const { getByRole } = render(HelloWorld)

    const input = getByRole('textbox', { name: 'Enter your username' })
    const button = getByRole('button', { name: 'Click me' })

    await userEvent.click(button)

    expect(input).not.toBeDisabled()
  })

  it('should greet the user', async () => {
    const { getByRole, getByText } = render(HelloWorld)

    const input = getByRole('textbox', { name: 'Enter your username' })
    const button = getByRole('button', { name: 'Click me' })

    await userEvent.click(button)
    await userEvent.type(input, 'Phil')

    expect(getByText('Hello Phil!')).toBeInTheDocument()
  })
})
