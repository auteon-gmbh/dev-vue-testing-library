import { mount } from '@vue/test-utils'
import HelloWorld from './HelloWorld.vue'

describe('Hello World', () => {
  it('should disable the input by default.', async () => {
    const wrapper = mount(HelloWorld)

    const input = wrapper.find('input')

    expect(input.attributes()).toHaveProperty('disabled')
  })

  it('should be possible to click the button', async () => {
    const wrapper = mount(HelloWorld)

    const button = wrapper.find('button')
    const input = wrapper.find('input')

    await button.trigger('click')

    expect(input.attributes()).not.toHaveProperty('disabled')
  })
})
