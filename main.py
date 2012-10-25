#!/usr/bin/env python
# coding: utf-8
import sys

def execute(filename):
	f = open(filename, 'r')
	evaluate(f.read().decode('UTF-8'))
	f.close()

def evaluate(code):
	memory = [0]
	cursor, ptr = 0, 0

	while ptr < len(code):
		command = code[ptr]

		if command == u'\u2630':
			cursor += 1
			if cursor == len(memory):
				memory.append(0)
		if command == u'\u2637':
			cursor -= 1
			if cursor < 0:
				cursor = 0
		if command == u'\u2633':
			memory[cursor] += 1
			if memory[cursor] > 255:
				memory[cursor] -= 256
		if command == u'\u2634':
			memory[cursor] -= 1
			if memory[cursor] < 0:
				memory[cursor] += 256
		if command == u'\u2635':
			sys.stdout.write(chr(memory[cursor]))
		if command == u'\u2632':
			memory[cursor] = ord(sys.stdin.read(1))
		if command == u'\u2636':
			if not memory[cursor]:
				depth = 0
				while ptr < len(code):
					if code[ptr] == u'\u2636':
						depth += 1
					if code[ptr] == u'\u2631':
						depth -= 1
					if depth == 0:
						break
					ptr += 1
		if command == u'\u2631':
			if memory[cursor]:
				depth = 0
				while ptr >= 0:
					if code[ptr] == u'\u2636':
						depth -= 1
					if code[ptr] == u'\u2631':
						depth += 1
					if depth == 0:
						break
					ptr -= 1

		ptr += 1

	

if __name__ == '__main__':
	if len(sys.argv) == 2:
		execute(sys.argv[1])
	else:
		print 'Usage: %s [filename]' % sys.argv[0]
