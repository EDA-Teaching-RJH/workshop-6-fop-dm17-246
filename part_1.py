sample_bay = ["Basalt", "Silica", "Iron", "Dust"]
print (sample_bay[0])
print(sample_bay[-1])
print(len(sample_bay))

x=3
sample_bay.remove(sample_bay[x])

for sample in sample_bay:
    print("Transmitting data for: " + sample)

new_findings = []

for findings in range(3):
    new_finding = input("Enter new finding: ")
    new_findings.append(new_finding.capitalize())

print("New findings: " + str(new_findings))

