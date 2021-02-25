import ephem

mars = ephem.Mars
const = ephem.constellation.now(mars)

print(const)