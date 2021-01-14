import { render, fireEvent } from '@testing-library/vue'
import HelloWorld from './HelloWorld-improved.vue'

describe('Hello World', () => {
  it('should disable the input by default.', async () => {
    const { getByRole } = render(HelloWorld)

    const input = getByRole('textbox', { name: 'Username' })

    expect(input).toBeDisabled()
  })

  it('should be possible to click the button', async () => {
    const { getByRole } = render(HelloWorld)

    const button = getByRole('button', { name: 'Click me' })
    const input = getByRole('textbox', { name: 'Username' })

    await fireEvent.click(button)

    expect(input).not.toBeDisabled()
  })
})
