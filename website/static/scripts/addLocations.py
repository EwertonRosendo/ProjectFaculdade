"""

locais = [
        ["Jaboatão dos Guararapes", -8.103842, -34.964894],
        ["Jaboatão dos Guararapes", -8.112111, -34.984333],
        ["Jaboatão dos Guararapes", -8.112838, -34.966134],
        ["Jaboatão dos Guararapes", -8.118601, -35.015874],
        ["Jaboatão dos Guararapes", -8.098355, -34.971742],
        ["Jaboatão dos Guararapes", -8.120693, -34.964022],
        ["Jaboatão dos Guararapes", -8.067852, -34.999433],
        ["Jaboatão dos Guararapes", -8.071622, -35.001066],
        ["Jaboatão dos Guararapes", -8.083102, -34.974252],
        ["Jaboatão dos Guararapes", -8.135951, -34.952849],
        ["Jaboatão dos Guararapes", -8.10852420, -34.96377820],
        ["Jaboatão dos Guararapes", -8.147619, -34.937078],
        ["Jaboatão dos Guararapes", -8.144151, -34.937500],
        ["Jaboatão dos Guararapes", -8.096741, -34.964340],

        ["Olinda", -7.984818, -34.899367],
        ["Olinda", -7.997594, -34.901971],
        ["Olinda", -7.995433, -34.898412],
        ["Olinda", -8.004337, -34.852533],
        ["Olinda", -7.994531, -34.852973],
        ["Olinda", -7.993544, -34.902047],
        ["Olinda", -7.979209, -34.851613],
        ["Olinda", -7.993176, -34.900670],
        ["Olinda", -7.977366, -34.903612],
        ["Olinda", -8.007290, -34.936464],
        ["Olinda", -7.979847, -34.907282],
        ["Olinda", -7.993244, -34.891755],
        ["Olinda", -7.985893, -34.861578],
        ["Olinda", -7.988932, -34.898067],
        ["Olinda", -7.993966, -34.890307]
    ]

    for local in locais:
        Scordenadas = {
            'city': local[0],
            'lat': str(local[1]),
            'long': str(local[2]),
        }
        location = Location(city=Scordenadas['city'], lat=Scordenadas['lat'], long=Scordenadas['long'])
        location.save()"""
