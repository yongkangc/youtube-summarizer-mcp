# YouTube Video Summary

**Source**: https://www.youtube.com/watch?v=Nn-SGblUhi4

## Summary

This is a panel discussion from a Linux Kernel Summit featuring Linus Torvalds, Alan Cox, and other kernel developers discussing the importance of userspace compatibility in Linux kernel development. The conversation explores the tension between maintaining backward compatibility (a core principle Linus has championed since the beginning) and the practical reality that the kernel occasionally breaks userspace APIs. The discussion delves into the philosophy behind compatibility decisions, how mistakes are handled, and the balance between supporting legacy systems while enabling innovation.

## Key Insights

### The Core Philosophy
- **User experience is paramount**: Linus's primary mantra is that breaking the user experience is the "absolute worst failure that a software project can make"
- **ABI stability follows from user experience**: The technical ABI stability requirement is a consequence of the user experience principle, not the primary goal itself
- **No project is more important than its users**: This principle guides all compatibility decisions

### The Version Number Case Study
- When Linux changed from major-minor-micro (2.6.x) to major-minor (3.x) versioning, some applications broke because they couldn't parse the new format
- Rather than reverting the change, the kernel team added a compatibility flag (`UNAME26`) that reports the version as "2.4.40" to legacy applications
- Linus acknowledged this was "idiotic" and "stupid" extra code, but felt so strongly about compatibility that they implemented it anyway
- This demonstrates the lengths they'll go to maintain compatibility even for "badly written" applications

### How Breakages Occur
- **Unintentional breaks**: Developers make improvements without considering that users rely on old behavior
- **Late discovery problem**: Sometimes breakage is noticed too late, after new applications have started depending on the new behavior, making reversion impossible
- **Security-driven breaks**: Sometimes interfaces are so badly designed they create security vulnerabilities and must be changed intentionally

### Handling Breakages
- When breakages are discovered, there's strong pressure to revert the problematic changes
- Linus is "not subtle" about telling developers when they've made mistakes
- The team actively works on tools to detect ABI changes made by mistake (PayPal was working on include file improvements for this)
- Deprecated interfaces are phased out gradually, giving users time to migrate

### The Deprecation Strategy
- Mark interfaces as deprecated
- Provide better replacement interfaces
- Discourage use of old interfaces
- Eventually remove old interfaces when usage drops
- If removal causes complaints, restore the interface

### Counterpoint: Acknowledged Breakages
- The moderator (Lennart Poettering) listed multiple examples where the kernel broke ABI without reverting:
  - sysfs was broken "many many times"
  - The ns cgroup controller was removed
  - These broke projects like systemd and VLC
- Linus acknowledged: "We make mistakes sometimes, we try to fix them very actively, and we don't lie about it"

### Enterprise vs. Consumer Perspectives
- Enterprise Linux users prioritize stability over features
- Their first question about new features: "Has it been running somewhere else reliably for three years?"
- This contrasts with hardware vendors who push for rapid adoption of new features

### Complexity Management
- Legacy compatibility layers rarely cause significant kernel complexity
- The real complexity comes from:
  - Supporting odd/bad hardware
  - Implementing complex algorithms for scalability and efficiency
  - The inherently complicated nature of what the kernel does
- Open source makes rewrites easier—they can change internal organization while maintaining legacy interfaces on top

### Security vs. Compatibility Tradeoffs
- Sometimes interfaces must be broken for security reasons
- The team tries to break things in ways that "normal users won't even notice"
- They attempt to limit information/access to prevent exploitation while maintaining apparent functionality for legitimate users

### Historical Testing Practices
- Linus used to run ancient a.out format binaries from the earliest Linux days to verify compatibility
- He tested deprecated system calls that were marked for removal within months of release
- This wasn't for practical use but to ensure those who wanted to use old binaries could

## Main Arguments or Thesis

**Linus's Position**: Userspace compatibility is not hypocritical—it's a genuine, strongly-held principle that guides kernel development. While breakages do occur, they are treated as serious failures that require immediate attention and remediation. The goal is not to prevent all change, but to ensure that all modes of working (old and new) continue to function.

**The Moderator's Challenge**: The principle may be somewhat self-serving for enterprise users who want to run old userspace with new kernels, and the long list of documented breakages suggests the "mantra" isn't always followed in practice.

**Alan Cox's Counterpoint**: The importance of stability is demonstrated by negative examples like GNOME 3.0, which showed "why you don't suddenly change everything on people who rely on what you were doing."

## Notable Quotes or Highlights

> "The biggest thing any program can do is not the technical details of the program itself—it's how useful the program is to users."
> — Linus Torvalds

> "No project is more important than the users of the project."
> — Linus Torvalds

> "There's a saying: on the Internet nobody can hear you being subtle. So I'm not subtle about it when I'm annoyed at someone."
> — Linus Torvalds, on how he handles developers who break compatibility

> "If you want to understand the importance of not suddenly changing your users' experience, I would go and take a look at GNOME 3.0."
> — Alan Cox

> "Has it been running somewhere else reliably for three years? That's the mentality of a lot of our user base."
> — Alan Cox, describing enterprise Linux users

> "We make mistakes sometimes, we try to fix them very actively, and we don't lie about it."
> — Linus Torvalds

## Practical Takeaways

1. **User experience trumps technical elegance**: When making design decisions, prioritize not breaking what users depend on
2. **Deprecation is a process, not an event**: Provide alternatives, discourage old usage, and remove only when adoption has shifted
3. **Compatibility layers are acceptable overhead**: Adding legacy support code is preferable to breaking existing users
4. **Be transparent about mistakes**: When breakages occur, acknowledge them and work actively to fix them
5. **Open source enables gradual evolution**: You can rewrite internals completely while maintaining stable external interfaces

## Additional Context

- This discussion took place at a Linux Kernel Summit, likely around 2011-2012 based on references to the Linux 3.0 version change
- The moderator appears to be Lennart Poettering (creator of systemd), who was personally affected by some kernel ABI breaks
- Paul McKenney (RCU maintainer) expressed concern about whether adding trace events would lock him into maintaining compatibility forever—Linus confirmed this is a real concern
- The Windows Sim City compatibility hack was mentioned as an example of going too far with compatibility fixes, though Linus didn't fully address where the line should be drawn
