// ///////////////////////////////////////////////////////
export function formatDate (timestamp) {
  const d = new Date(timestamp)
  const time = d.toLocaleTimeString('en-US')
  return time.substr(0, 5) + time.slice(-2) + ' | ' + d.toLocaleDateString()
}


////////////////////////////////

function generateUID () {
  return Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15)
}

export function formatQuestion ({ optionOneText, optionTwoText, author }) {
  return {
    id: generateUID(),
    timestamp: Date.now(),
    author,
    optionOne: {
      votes: [],
      text: optionOneText,
    },
    optionTwo: {
      votes: [],
      text: optionTwoText,
    }
  }
}

export function truncateText (str) {
  return str.length > 30 ? "..." + str.substring(0, 7) + "..." : "..." + str + "...";
}

export function idToList(list){
  let resultList = {}
  for (let item in list){
    resultList[list[item].id]=list[item]
  }
  return resultList
}

export function tableColumnsArray(list){
  console.log(list)
  let resultList = []
  for (let item in list){
    resultList.push(list[item].COLUMN_NAME)
  }
  return resultList
}

export function capitalizeFirstLetter(string) {
  return string.slice(0, 1).toUpperCase() + string.slice(1);
}

export function order_dict(dict, options_dict=false){
  let data = Object.entries(dict)
  let ordered_data = data && data.filter(([key, val])=>key.toLowerCase().includes("id") && !key.toLowerCase().includes("name"))
  .concat(data.filter(([key, val])=>key.toLowerCase().includes("name")))
  .concat(data.filter(([key, val])=>key.toLowerCase().includes("desc")))
  .concat(data.filter(([key, val])=>!key.toLowerCase().includes("name") && !key.toLowerCase().includes("id") && !key.toLowerCase().includes("desc") && (options_dict ? !val.type.includes("many") : typeof val != "object")))
  .concat(data.filter(([key, val])=>!key.toLowerCase().includes("name") && !key.toLowerCase().includes("id") && !key.toLowerCase().includes("desc") && (options_dict ? val.type.includes("many") : typeof val == "object")))

  return ordered_data
}