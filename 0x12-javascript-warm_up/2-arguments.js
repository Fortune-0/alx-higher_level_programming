#!/user/bin/node

const  argsLength = process.argv.Length;

if (argsLength === 2)
{
	console.log('No arguments');
}
else if (argsLength === 3)
{
	console.log('Argument found');
}
else
{
	console.log('Arguments found');
}

