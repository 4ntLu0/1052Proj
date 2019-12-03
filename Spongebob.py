from buzzer_player import *
def spongebob_melody():
	sponge_bob_melody = [
		notes['D5'],
		notes['Df'],notes['D5'],notes['E5'],notes['D5'],notes['B4'],notes['G3'],notes['B4'],notes['D5'],notes['E5'],notes['D5'],notes['B4'],
		notes['D3'],notes['D3'],notes['D3'],notes['D3'],
		notes['D5'],notes['G3'],notes['G3'],notes['G3'],notes['G3'],notes['E5'],notes['E5'],notes['E5'],notes['G3'],notes['G3'],notes['G3'],
		notes['C5'],notes['C5'],notes['C5'],notes['C5'],
		notes['B4'],notes['D5'],notes['E5'],notes['D5'],notes['B4'],notes['G3'],notes['B4'],notes['D5'],notes['E5'],notes['D5'],notes['B4'],
		notes['D3'],notes['D3'],notes['D3'],notes['D3'],
		notes['E5'],notes['G3'],notes['G3'],notes['G3'],notes['G3'],notes['E5'],notes['G3'],notes['E5'],notes['E5'],notes['G3'],
		notes['C5'],notes['C5'],notes['C5'],notes['C5'],
		notes['G3'],notes['E5'],notes['D3'],notes['B4'],
		notes['G3'],notes['E5'],notes['D3'],notes['B4'],
		notes['G3'],notes['E5'],notes['D3'],notes['B4'],
		notes['D3'],notes['E5'],notes['F5'],notes['G3'],
		notes['B4'],notes['A4'],notes['B4'],notes['A4'],notes['G3'],notes['A4'],notes['B4'],notes['G3'],
		notes['G3'],notes['A4'],notes['B4'],notes['A4'],notes['G3'],notes['D3'],notes['G3']
		
	
	]
	
	sponge_bob_tempo = [
		1,
		1,16,16,4,4,
		1,16,16,8,8,4,
		1,16,16,4,4,
		2,4,16,16,8,8,8,8,
		4,4,16,16,4,4,
		1,16,16,8,8,4,
		1,16,16,4,4,
		2,4,16,16,8,8,8,8,
		4,16,16,4,16,16,
		8,8,8,8,4,4,
		2,8,4,16,16,
		1,
	]
	




try:
	setup()
	print("Spongebob theme")
	play(sponge_bob_melody, sponge_bob_tempo, 0.30, 1.2000)
	time.sleep(2)
	destroy()
except KeyboardInterrupt:  	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
	destroy()	