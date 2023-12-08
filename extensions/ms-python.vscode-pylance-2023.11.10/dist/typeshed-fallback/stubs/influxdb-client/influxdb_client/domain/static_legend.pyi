from _typeshed import Incomplete

class StaticLegend:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        colorize_rows: Incomplete | None = None,
        height_ratio: Incomplete | None = None,
        show: Incomplete | None = None,
        opacity: Incomplete | None = None,
        orientation_threshold: Incomplete | None = None,
        value_axis: Incomplete | None = None,
        width_ratio: Incomplete | None = None,
    ) -> None: ...
    @property
    def colorize_rows(self): ...
    @colorize_rows.setter
    def colorize_rows(self, colorize_rows) -> None: ...
    @property
    def height_ratio(self): ...
    @height_ratio.setter
    def height_ratio(self, height_ratio) -> None: ...
    @property
    def show(self): ...
    @show.setter
    def show(self, show) -> None: ...
    @property
    def opacity(self): ...
    @opacity.setter
    def opacity(self, opacity) -> None: ...
    @property
    def orientation_threshold(self): ...
    @orientation_threshold.setter
    def orientation_threshold(self, orientation_threshold) -> None: ...
    @property
    def value_axis(self): ...
    @value_axis.setter
    def value_axis(self, value_axis) -> None: ...
    @property
    def width_ratio(self): ...
    @width_ratio.setter
    def width_ratio(self, width_ratio) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
