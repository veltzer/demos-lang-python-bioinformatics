-- python deps for this project

dofile("config/shared.lua")

-- append every element of "src" onto "dst"
local function extend(dst, src)
    for _, value in ipairs(src) do
        table.insert(dst, value)
    end
    return dst
end

INSTALL_REQUIRES = {
    "biopython",
    "numpy",
    "pandas",
    "scipy",
    "matplotlib",
    "seaborn",
}
BUILD_REQUIRES = BUILD
TEST_REQUIRES = TEST
TYPES_REQUIRES = {
    "types-PyYAML",
    "pandas-stubs",
}

REQUIRES = {}
extend(REQUIRES, INSTALL_REQUIRES)
extend(REQUIRES, BUILD_REQUIRES)
extend(REQUIRES, TEST_REQUIRES)
extend(REQUIRES, TYPES_REQUIRES)
