import shlex
import subprocess


def run_cmd(command):
	"""
	Demonstrate usage of
		* shlex
		* Executing CLI command and printing output
	:param command:
	:return:
	"""
	print('--> ' + command)

	# use shlex to split shell like commands: command -a -b -c -d -e
	args = shlex.split(command)

	proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	# Print all the  process output after it is finished
	out, err = proc.communicate()
	proc.wait()
	print(out)
	print('Exit code: ', proc.returncode)

	# Alternatively, print hte process out in real-time
	with proc.stdout as output:
		for line in iter(output.readline, b''):
			print('Process output: ', line)
	print('Exit code: ', proc.returncode)


if __name__ == '__main__':
	run_cmd('ls -l -a -h -t -r')
