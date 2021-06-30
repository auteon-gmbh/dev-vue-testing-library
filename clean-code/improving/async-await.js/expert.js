const readline = require('readline')

function askQuestion(question) {
  const readlineInterface = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  })
  return new Promise(resolve => {
    readlineInterface.question(question, answer => {
      resolve(answer)
      readlineInterface.close()
    })
  })
}

async function main() {
  const name = await askQuestion("What is your name? ")
  const job = await askQuestion("What is your job? ")
  const age = await askQuestion("How old are you? ")

  console.log(`Hello ${name}. You are a ${age} year old ${job}.`)
}
main()