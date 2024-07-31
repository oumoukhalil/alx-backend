import { createClient, print } from 'redis'
import { promisify } from 'util'

const client = createClient()
client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`)
})

client.on('connect', () => { 
  console.log("Redis client connected to the server")
})

function setNewSchool(schoolName, value) {
     client.set(schoolName, value, print)
}

async function displaySchoolValue(schoolName) {
     const getValue = promisify(client.get).bind(client)
     const value = await getValue(schoolName)
     console.log(value)
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
