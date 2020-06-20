# sensor.umea_kommun_water_temperature
Provides water temperature sensors for different places in Umeå kommun. The places are

- Bettnessand
- Bölesholmarna
- Kärleksviken
- Länkebo
- Ljumviken
- Stöcksjön
- Nydalabadet

### Installation
Copy the `umea_kommun_water_temperature` folder into your `custom_components` folder.

Add the following to your `configuration.yaml` file:

```yaml
sensor:
  - platform: umea_kommun_water_temperature
    scan_interval: 300 # every 5 minutes should suffice
```
