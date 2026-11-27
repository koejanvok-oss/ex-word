"""One word from your ex: "Avoidant".

Why an ex would say it: emotionally unavailable, vanishes the moment
things get real, then acts surprised when the door closes behind them.
The clinical word every ex reaches for — it stings because it is true,
and the person hearing it knows exactly why it fits.
"""

import os


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write("Avoidant")


if __name__ == "__main__":
    main()
