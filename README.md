## Customize Actions
- When you use expressions in an if conditional, you may omit the ${{ }} expression syntax because GitHub Actions automatically evaluates the if conditional as an expression. However, this rule does not apply everywhere.

- You must use the ${{ }} expression syntax or escape with '', "", or () when the expression starts with !, since ! is reserved notation in YAML format.

- Using the ${{ }} expression syntax turns the contents into a string, and strings are truthy. For example, if: true && ${{ false }} will evaluate to true.
