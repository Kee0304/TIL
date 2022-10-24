const savedFile = {
  name: 'profile',
  extension: 'jpg',
  size: 29930
}

function fileSummary(file) {
  const { name, extension, size } = file;
  console.log(`The file ${name}.${extension} is size of ${size} bytes.`)
}

fileSummary(savedFile)