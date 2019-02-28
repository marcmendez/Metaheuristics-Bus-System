data = None

data_0 = {
	'numBuses': 2,
	'numDrivers': 2,
	'numServices': 2,
	'maxBuses': 1,
	'BM': 40,
	'CBM': 1,
	'CEM': 3,

	'startTime': [0, 60],
	'minutesDuration': [30, 50],
	'kmDuration': [40, 35],
	'passangers': [50, 30],

	'capacity': [60, 40],
	'eurosMin': [4, 5],
	'eurosKm': [3, 2],

	'maxMinutes': [60, 40],

}

data_1 = {
	'numBuses': 3,
	'numDrivers': 3,
	'numServices': 3,
	'maxBuses': 2,
	'BM': 40,
	'CBM': 2,
	'CEM': 3,

	'startTime': [0, 60, 70],
	'minutesDuration': [30, 50, 15],
	'kmDuration': [40, 35, 20],
	'passangers': [50, 30, 20],

	'capacity': [60, 40, 25],
	'eurosMin': [3, 2, 2],
	'eurosKm': [3, 2, 2],

	'maxMinutes': [60, 40, 50],

}

data_2 = {
	'numBuses': 20,
	'numDrivers': 20,
	'numServices': 30,
	'maxBuses': 20,
	'BM': 480,
	'CBM': 0.15,
	'CEM': 0.3,

	'startTime': [420, 420, 435, 435, 450, 450, 465, 465, 480, 480, 510, 510, 540, 540, 600, 600, 660, 660, 720, 720, 780, 780, 900, 900, 960, 960, 975, 975, 990, 990],
	'minutesDuration': [45, 45, 45, 45, 45, 45, 45, 45, 20, 20, 20, 20, 60, 60, 60, 60,  60, 60, 60, 60, 90, 90, 90, 90, 90, 90, 90, 90, 15, 15],
	'kmDuration': [20, 20, 20, 20, 20, 20, 20, 20, 15, 15,  15, 15, 30, 30, 30, 30, 30, 30, 30, 30, 40, 40, 40, 40,  40, 40, 40, 40, 15, 15],
	'passangers': [50, 50, 50, 50, 50, 50, 50, 50, 30, 30, 30, 30, 75, 75, 75, 75, 75, 75, 75, 75, 80, 80, 80, 80, 80, 80, 80, 80, 30, 30],

	'capacity': [85, 85, 85, 85, 85, 85, 75, 75, 75, 75, 75, 75, 60, 60, 60, 60, 30, 30, 30, 30 ],
	'eurosMin': [5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 2.5, 2.5, 2.5, 2.5, 2, 2 ,2, 2],
	'eurosKm': [5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 2.5, 2.5, 2.5, 2.5, 2, 2, 2, 2],

	'maxMinutes': [140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140],

}



data_3 = {
	'numBuses': 20,
	'numDrivers': 20,
	'numServices': 50,
	'maxBuses': 12,
	'BM': 480,
	'CBM': 0.15,
	'CEM': 0.3,

	'startTime': [420, 420, 430, 435, 435, 440, 450, 450, 455, 460, 465, 465, 470, 470, 480, 480, 490, 490, 510, 510, 520, 530, 540, 540, 550, 560, 570, 580, 590, 600, 600, 660, 660, 720, 720, 780, 780, 900, 900, 960, 960, 975, 975, 990, 990, 1020, 1020, 1050, 1060, 1060],
	'minutesDuration': [65, 65, 65, 65, 45, 45, 45, 45, 45, 45, 45, 45, 45, 40, 40, 40, 20, 20, 20, 20, 60, 60, 60, 70, 70, 80, 80, 60, 60, 60, 60, 60, 60, 60, 60, 60, 100, 90, 90, 110, 90, 90, 90, 90, 90, 90, 90, 90, 15, 15],
	'kmDuration': [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 15, 15, 15, 15, 15, 15, 15, 15, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 40, 30, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 15, 15, 15, 15],
	'passangers': [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 30, 30, 30, 30, 30, 30, 30, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 30, 30, 30, 30, 30],

	'capacity': [85, 85, 85, 85, 85, 85, 75, 75, 75, 75, 75, 75, 60, 60, 60, 60, 30, 30, 30, 30 ],
	'eurosMin': [5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 2.5, 2.5, 2.5, 2.5, 2, 2 ,2, 2],
	'eurosKm': [5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 2.5, 2.5, 2.5, 2.5, 2, 2, 2, 2],

	'maxMinutes': [240, 240, 240, 240, 240, 240, 240, 240, 240, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140],

}