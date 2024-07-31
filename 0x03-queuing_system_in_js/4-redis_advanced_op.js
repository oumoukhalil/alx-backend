import { createClient } from 'redis'

const client = createClient()
const schools = {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2 
}
for(let city of Object.keys(schools)) {
client.hmset('HolbertonSchools', city, schools[city], (err, reply) => {
if(reply) {
  console.log('Reply: 1')
}
})

}
client.hgetall('HolbertonSchools', (err, getDatas) => { 
console.log(getDatas)
})
