# ClicksCities


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `city`                                                                           | *str*                                                                            | :heavy_check_mark:                                                               | The name of the city                                                             |
| `country`                                                                        | [components.ClicksCitiesCountry](../../models/components/clickscitiescountry.md) | :heavy_check_mark:                                                               | The 2-letter country code of the city: https://d.to/geo                          |
| `clicks`                                                                         | *float*                                                                          | :heavy_check_mark:                                                               | The number of clicks from this city                                              |